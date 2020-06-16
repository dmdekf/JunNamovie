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
      "525887776863-23ne2tiqrvn3d12sdefpc6bu7bqh97oe.apps.googleusercontent.com",
    redirect_uri: "http://127.0.0.1:8000/accounts/google/login/callback/",
    scope: "https://www.googleapis.com/auth/contacts.readonly",
  };
  url = buildUrl("https://accounts.google.com/o/oauth2/v2/auth", params);
  location.replace(url);
}
