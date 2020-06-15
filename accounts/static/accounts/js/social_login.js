function buildQuery(params) {
  return Object.keys(params)
    .map(function (key) {
      return key + "=" + encodeURIComponent(params[key]);
    })
    .join("&");
}
function buildUrl(baseUrl, queries) {
  return baseUrl + "?" + buildQuery(queries);
}

function googleLogin() {
  print("----------------");
  params = {
    response_type: "code",
    client_id:
      "525887776863-6hlane191e75rv8pis7vi05st3j0rfci.apps.googleusercontent.com",
    redirect_uri: "http://127.0.0.1:8000/accounts/google/login/callback/",
    scope: "https://www.googleapis.com/auth/contacts.readonly",
    state: document.querySelector("[name=csrfmiddlewaretoken]").value,
  };
  url = buildUrl("https://accounts.google.com/o/oauth2/v2/auth", params);
  location.replace(url);
  print("--####################------");
}
