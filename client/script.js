"use sctrict";

const BACKEND = "http://127.0.0.1:8000"; // change it if server uses different port!!
let file = null;
const fileInput = document.getElementById("file-input");
const fileInputConteiner = document.getElementById("upload-file-container");
const submitBtn = document.getElementById("submit-button");
const form = document.getElementById("form");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  await getResults();
});

const messageBox = document.getElementById("upload-file-message");
fileInputConteiner.addEventListener("click", () => {
  openUploadFile();
});

fileInput.addEventListener("change", (e) => {
  if (e.target.files.length === 0) {
    messageBox.textContent = "No file selected";
    return;
  }
  messageBox.textContent = e.target.files[0].name;
  file = e.target.files[0];
});

function openUploadFile() {
  fileInput.click();
}

async function getResults() {
  if (file === null) {
    messageBox.textContent = "Pleas select file from local";
    return;
  }
  try {
    const formData = new FormData();
    formData.append("img", file);
    console.log("trying fetch data");
    const res = await fetch(`${BACKEND}/skin-can/detector`, {
      method: "POST",
      body: formData,
    });
    const json = await res.json();
    messageBox.textContent = json.result;
  } catch (e) {
    console.log(e);
  }
}
