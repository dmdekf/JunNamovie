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
  params = {
    response_type: "code",
    client_id:
      "525887776863-6hlane191e75rv8pis7vi05st3j0rfci.apps.googleusercontent.com",
    redirect_uri: "http://127.0.0.1:8000/accounts/google/login/callback/",
    state: document.querySelector("[name=csrfmiddlewaretoken]").value,
  };
  url = buildUrl(
    "https://accounts.google.com/signin/oauth/oauthchooseaccount",
    params
  );
  location.replace(url);
}
