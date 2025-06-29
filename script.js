// Author: Shehryar

// Toggle View Logic
function showOrganizer() {
  document.getElementById("organizerSection").style.display = "block";
  document.getElementById("inviteeSection").style.display = "none";
}

function showInvitee() {
  document.getElementById("organizerSection").style.display = "none";
  document.getElementById("inviteeSection").style.display = "block";
}

// ==========================
// Organizer Poll Form Logic
// ==========================
document.getElementById("pollForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const organizerName = document.getElementById("organizerName").value.trim();
  const eventTitle = document.getElementById("eventTitle").value.trim();
  const datesRaw = document.getElementById("dates").value.trim();

  const dates = datesRaw
    .split("\n")
    .map((date) => date.trim())
    .filter((date) => date !== "");

  const resultDiv = document.getElementById("result");

  let html = `
    <h3>Poll Created</h3>
    <p><strong>Organizer:</strong> ${organizerName}</p>
    <p><strong>Event:</strong> ${eventTitle}</p>
    <p><strong>Dates:</strong></p>
    <ul>
      ${dates.map((date) => `<li>${date}</li>`).join("")}
    </ul>

    <hr>

    <h3>Invitee Response</h3>
    <form id="inviteeForm">
      <label for="inviteeName">Your Name:</label><br />
      <input type="text" id="inviteeName" name="inviteeName" required /><br /><br />
      ${dates
        .map(
          (date, index) => `
        <label>${date}:</label>
        <select name="response-${index}">
          <option value="yes">Yes</option>
          <option value="no">No</option>
        </select><br /><br />
      `
        )
        .join("")}
      <button type="submit">Submit Response</button>
    </form>

    <div id="inviteeResult" style="margin-top: 20px;"></div>
  `;

  resultDiv.innerHTML = html;

  const allResponses = [];

  setTimeout(() => {
    const inviteeForm = document.getElementById("inviteeForm");
    inviteeForm.addEventListener("submit", function (e) {
      e.preventDefault();

      const name = document.getElementById("inviteeName").value.trim();
      const responses = dates.map((_, index) => {
        const val = document.querySelector(
          `select[name="response-${index}"]`
        ).value;
        return `${dates[index]}: ${val}`;
      });

      allResponses.push({ name, responses });

      const output = allResponses
        .map(
          (entry, i) => `
          <div style="margin-bottom: 20px;">
            <h4>Response #${i + 1}</h4>
            <p><strong>Name:</strong> ${entry.name}</p>
            <ul>${entry.responses.map((r) => `<li>${r}</li>`).join("")}</ul>
          </div>
        `
        )
        .join("");

      document.getElementById("inviteeResult").innerHTML = output;
      inviteeForm.reset();
    });
  }, 100);
});

// ==========================
// Static RSVP Form + CSV Export
// ==========================
const rsvpResponses = [];

document.getElementById("inviteForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const rsvp = document.getElementById("rsvp").value;

  if (name && rsvp) {
    rsvpResponses.push({ name, rsvp });
    alert("RSVP response recorded!");

    document.getElementById("name").value = "";
    document.getElementById("rsvp").value = "";
  }
});

document.getElementById("downloadBtn").addEventListener("click", function () {
  if (rsvpResponses.length === 0) {
    alert("No RSVP responses to export.");
    return;
  }

  const csvHeader = "Name,RSVP\n";
  const csvRows = rsvpResponses.map((r) => `${r.name},${r.rsvp}`).join("\n");
  const blob = new Blob([csvHeader + csvRows], { type: "text/csv" });

  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "invite_responses.csv";
  a.click();
  URL.revokeObjectURL(a.href);
});
