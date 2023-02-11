function selectListUsingUrlParam() {
    const params = new URLSearchParams(window.location.search)
    const list = params.get("list")
    if (!list) return

    selectElement = document.querySelector('select[name="list"]')
    if (!selectElement) return
    selectElement.value = parseInt(list)
}

window.onload = selectListUsingUrlParam
