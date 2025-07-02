/*
 * File: header.js
 * Author: Ragib Asif
 * Email: ragib.asif30@myhunter.cuny.edu
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 */

import { externalLink } from "./utils.js";

const TITLE = "SORTER";
const TITLE_EXPANDED = "SORT Event Resource";
const DESCRIPTION_BRIEF =
  "A web based availability tool for event organizers or management teams who need to find a common date for an event for any number of people.";
const DESCRIPTION_EXPANDED =
  "SORT Event Resource (SORTER) provides simple tools to invitees, and significantly more robust options for organizers, unlike other services such as WhenAvailable or DatePoll. Our product provides weighting and comparison in order to prioritize participants based on the meaningfulness of their contribution while providing an obfuscated front end that is more friendly to attendees.";

export const header = function () {
  const header = document.getElementById("header-container");
  header.classList.add("container");

  const title = document.createElement("h1");
  title.innerText = TITLE;
  header.appendChild(title);

  const title_expanded = document.createElement("h2");
  title_expanded.innerText = TITLE_EXPANDED;
  header.appendChild(title_expanded);

  const description_brief = document.createElement("p");
  description_brief.innerText = DESCRIPTION_BRIEF;
  description_brief.classList.add("paragraph");
  header.appendChild(description_brief);

  const description_expanded = document.createElement("p");
  description_expanded.innerText = DESCRIPTION_EXPANDED;
  description_expanded.classList.add("paragraph");
  header.appendChild(description_expanded);
};
