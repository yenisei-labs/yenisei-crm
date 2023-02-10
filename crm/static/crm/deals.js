'use strict'

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
