'use strict'

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
