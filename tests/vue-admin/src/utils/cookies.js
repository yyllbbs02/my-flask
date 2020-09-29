import Cookies from 'js-cookie'
const adminTokenKey = 'adminTokenKey_product'
export function setCookies(key, val) {
  return Cookies.set(key, val)
}
export function setCookiesByExpir(key, val, expires) {
  return Cookies.set(key, val, { expires: expires })
}
export function getCookies(key) {
  return Cookies.get(key)
}

export function removeCookies(key) {
  return Cookies.remove(key)
}
export function getCookiesByJson(key) {
  return Cookies.getJSON(key)
}
export function getCookiesListByJson() {
  return Cookies.getJSON()
}
export function getCookiesList() {
  return Cookies.get()
}

export function getAdminToken() {
  return Cookies.get(adminTokenKey)
}
export function setAdminToken(val) {
  return Cookies.set(adminTokenKey, val)
}
export function removeAdminToken() {
  return Cookies.remove(adminTokenKey)
}
