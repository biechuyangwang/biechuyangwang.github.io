const DEFAULT_SERVER_URL = "http://120.24.4.30:4399";

if (!localStorage.getItem("server_url")) {
  localStorage.setItem("server_url", DEFAULT_SERVER_URL);
}

window.SERVER_URL = localStorage.getItem("server_url");
window.enableSettingsPage = true;
