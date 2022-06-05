export default function AuthHeader() {
  const user = JSON.parse(localStorage.getItem("user"));

  if (user && user.token) {
    return { 'X-Access-Token': user.token };       // for Flask / Node.js Express back-end
      //  return { "Authorization": "Bearer " + user.token }; // for other
  } else {
    return {};
  }
}
