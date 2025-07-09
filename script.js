// Toggle View Logic
function showOrganizer() {
  document.getElementById("organizerSection").style.display = "block";
  document.getElementById("inviteeSection").style.display = "none";
}

function showInvitee() {
  document.getElementById("organizerSection").style.display = "none";
  document.getElementById("inviteeSection").style.display = "block";
}

let allResponses = [];
let currentDates = [];

document.getElementById("pollForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const organizerName = document.getElementById("organizerName").value.trim();
  const eventTitle = document.getElementById("eventTitle").value.trim();
  let datesRaw = document.getElementById("dates").value.trim();
  currentDates = datesRaw.split("\n").map((date) => date.trim()).filter((date) => date !== "");

  // Basic date format validation (MM/DD/YYYY)
  const dateRegex = /^\d{2}\/\d{2}\/\d{4}$/;
  if (!currentDates.every((date) => dateRegex.test(date))) {
    alert("Please use MM/DD/YYYY format for all dates.");
    return;
  }

  document.getElementById("result").innerHTML = `
    <h3>Poll Created</h3>
    <p><strong>Organizer:</strong> ${organizerName}</p>
    <p><strong>Event:</strong> ${eventTitle}</p>
    <p><strong>Dates:</strong></p>
    <ul>${currentDates.map((date) => `<li>${date}</li>`).join("")}</ul>
  `;

  // Update inviteeSection form
  const inviteeForm = document.getElementById("inviteForm");
  inviteeForm.innerHTML = `
    <label for="name">Invitee Name:</label><br />
    <input type="text" id="name" required /><br /><br />
    ${currentDates.map((date, index) => `
      <label>${date}:</label>
      <select name="response-${index}" required>
        <option value="">--Select--</option>
        <option value="Yes">Yes</option>
        <option value="No">No</option>
      </select><br /><br />
    `).join("")}
    <button type="submit">Submit RSVP</button>
  `;
  allResponses = [];
  document.getElementById("downloadBtn").disabled = true;
});

document.getElementById("inviteForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  if (!name) return;

  const responses = currentDates.map((_, index) => {
    const select = document.querySelector(`select[name="response-${index}"]`);
    return select.value || "No Response";
  });

  allResponses.push({ name, responses });
  document.getElementById("inviteeResult").innerHTML = allResponses.map((entry, i) => `
    <div class="response-item"><h4>Response #${i + 1}</h4><p>Name: ${entry.name}</p><ul>${entry.responses.map((resp, i) => `<li>${currentDates[i]}: ${resp}</li>`).join("")}</ul></div>
  `).join("");
  e.target.reset();
  document.getElementById("downloadBtn").disabled = false;
});

document.getElementById("downloadBtn").addEventListener("click", function () {
  if (allResponses.length === 0) {
    alert("No invitee responses to export.");
    return;
  }

  let csvHeader = "Name," + currentDates.join(",") + "\n";
  let csvRows = allResponses.map((entry) => [entry.name, ...entry.responses].join(",")).join("\n");
  const blob = new Blob([csvHeader + csvRows], { type: "text/csv" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "invitee_poll_responses.csv";
  a.click();
  URL.revokeObjectURL(a.href);
});