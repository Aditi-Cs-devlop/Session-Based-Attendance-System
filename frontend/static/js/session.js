// ===== GET ELEMENTS =====
const startBtn = document.getElementById("startSession");
const stopBtn = document.getElementById("stopSession");
const captureBtn = document.getElementById("captureBtn");
const recaptureBtn = document.getElementById("recaptureBtn");
const cameraStatus = document.getElementById("cameraStatus");

const totalFaces = document.getElementById("totalFaces");
const recognized = document.getElementById("recognized");
const unrecognized = document.getElementById("unrecognized");

// ===== SESSION STATE =====
let sessionActive = false;

// ===== START SESSION =====
startBtn.addEventListener("click", () => {
    sessionActive = true;

    cameraStatus.innerText = "Camera Enabled";
    cameraStatus.style.background = "#e6fcf5";

    startBtn.disabled = true;
    stopBtn.disabled = false;

    captureBtn.disabled = false;
    recaptureBtn.disabled = true;
});

// ===== STOP SESSION =====
stopBtn.addEventListener("click", () => {
    sessionActive = false;

    cameraStatus.innerText = "Camera Disabled";
    cameraStatus.style.background = "#ecf0f3";

    startBtn.disabled = false;
    stopBtn.disabled = true;

    captureBtn.disabled = true;
    recaptureBtn.disabled = true;

    totalFaces.innerText = "0";
    recognized.innerText = "0";
    unrecognized.innerText = "0";
});

// ===== CAPTURE IMAGE =====
captureBtn.addEventListener("click", () => {
    if (!sessionActive) return;

    // Dummy API result
    const total = Math.floor(Math.random() * 5) + 1;
    const recog = Math.floor(Math.random() * total);
    const unrecog = total - recog;

    totalFaces.innerText = total;
    recognized.innerText = recog;
    unrecognized.innerText = unrecog;

    captureBtn.disabled = true;
    recaptureBtn.disabled = false;

    cameraStatus.innerText = "Image Captured";
});

// ===== RE-CAPTURE =====
recaptureBtn.addEventListener("click", () => {
    if (!sessionActive) return;

    captureBtn.disabled = false;
    recaptureBtn.disabled = true;

    cameraStatus.innerText = "Camera Enabled";
});
