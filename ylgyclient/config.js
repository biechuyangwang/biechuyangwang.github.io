const DEFAULT_SERVER_URL = "http://38.34.244.41:1357";

if (!localStorage.getItem("server_url")) {
  localStorage.setItem("server_url", DEFAULT_SERVER_URL);
}

window.SERVER_URL = localStorage.getItem("server_url");
window.enableSettingsPage = true;
