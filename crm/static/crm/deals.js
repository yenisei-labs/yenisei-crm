'use strict'

async function saveOrder(listId, order, csrfToken) {
    if (listId == "-1") return // deals without list

    let i = 0
    for (const dealId of order) {
        const formData = new FormData()
        formData.append("order", i)
        formData.append("list", listId)

        const options = {
            method: "POST", // django doesn't understand PATCH?
            headers: {
                'X-CSRFToken': csrfToken,
            },
            body: formData
        }

        const url = `/crm/api/deals/${dealId}/`
        const res = await fetch(url, options)
        if (!res.ok) alert("Save order: request failed")
        i++;
    }
}

function createSortableLists() {
    const lists = document.querySelectorAll(".sortable-deal-list")
    window.sortables = []
    for (const list of lists) {
        const sortable = new Sortable(list, {
            group: 'shared',
            animation: 100,
            ghostClass: 'ghost-deal',
            store: {
		        /**
		         * Save the order of elements. Called onEnd (when the item is dropped).
		         * @param {Sortable}  sortable
		         */
		        set: (sortable) => {
                    const listId = sortable.el.attributes['data-id'].value
                    const csrfToken = sortable.el.attributes['csrf'].value
			        const order = sortable.toArray()
                    saveOrder(listId, order, csrfToken)
		        }
	        },
        });
        window.sortables.push(sortable)
    }
}

window.onload = createSortableLists

async function patch_deal_list(event, list_id, csrf_token) {
    event.preventDefault()

    const fd = new FormData()
    fd.append('title', event.target.title.value)

    const url = `/crm/api/lists/${list_id}/`
    const options = {
        method: "POST", // django doesn't understand PATCH?
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: fd,
    }
    const res = await fetch(url, options)

    if (!res.ok) {
        alert("Something went wrong")
        console.log(res)
        return
    }
}

async function delete_deal_list(csrf_token, list_id) {
    const confirmation = confirm("Do you really want to delete this list?")
    if (!confirmation) return

    const url = `/crm/api/lists/${list_id}/`
    const options = {
        method: "DELETE",
        headers: {
            'X-CSRFToken': csrf_token,
        },
    }
    const res = await fetch(url, options)

    if (!res.ok) {
        console.log("delete_deal_list: something went wrong")
        console.log(res)
        return
    }

    window.location.reload()
}
