"use sctrict";

const BACKEND = "";
const file = null;
const fileInput = document.getElementById("file-input");
const fileInputConteiner = document.getElementById("upload-file-container");

const messageBox = document.getElementById("upload-file-message");
fileInputConteiner.addEventListener("click", () => {
  fileInput.click();
});

fileInput.addEventListener("change", (e) => {
  if (e.target.files.length === 0) {
    messageBox.textContent = "No file selected";
    return;
  }
  messageBox.textContent = e.target.files[0].name;
  file = e.target.files[0];
});

async function getResults() {
  if (file === null) {
    messageBox.textContent = "Pleas select file from local";
  }
  try {
    await fetch(`${BACKEND}/skin-can/detector`, {
      method: "POST",
      body: file,
    });
  } catch (e) {
    console.log(e);
  }
}
