function selectListUsingUrlParam() {
    const params = new URLSearchParams(window.location.search)
    const list = params.get("list")
    if (!list) return

    selectElement = document.querySelector("#id_list")
    selectElement.value = parseInt(list)
}

window.onload = selectListUsingUrlParam
