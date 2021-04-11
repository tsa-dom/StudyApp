const get = (id) => {
  return document.getElementById(id)
}
const toggleVisibility = (id1, id2) => {
  const visibility = get(id1).style.display
  get(id1).style.display = get(id2).style.display
  get(id2).style.display = visibility 
}
const fire = (id, action) => {
  event.preventDefault()
  get(id).action = action
  get(id).submit()
}
const setMessage = (element, message) => {
  element.style.display = ""
  element.innerHTML = message
  setTimeout(() => {
    element.style.display = "none"
  }, 5000)
}