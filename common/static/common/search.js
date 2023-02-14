async function search(e) {
    const container = document.querySelector("#search-container")
    
    const query = e.target.value
    if (query === "") {
        container.innerHTML = ""
        return
    }

    const url = `/api/search/${query}/`
    const res = await fetch(url)
    if (!res.ok) return
    const results = await res.json()

    container.innerHTML = ""
    for (const entry of results) {
        const element = document.createElement("a")
        const text = document.createTextNode(entry.title)
        element.appendChild(text)
        element.href = entry.url
        container.appendChild(element)
    }
}
