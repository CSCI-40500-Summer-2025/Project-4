/*
 * File: footer.js
 * Author: Ragib Asif
 * Email: ragib.asif30@myhunter.cuny.edu
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 */

import { externalLink } from "./utils.js";

const NAME = "Ragib Asif, Jason Ongjoco";

const YEAR = new Date().getFullYear();

const SOCIALS = [
  {
    name: "GitHub",
    url: "https://github.com/CSCI-40500-Summer-2025/Project-4",
  },
];

const CONTAINERS = {
  socials: "socials-container",
  copyright: "copyright-container",
};

const renderSocials = function () {
  const socialsContainer = document.getElementById(CONTAINERS.socials);
  const socialsList = document.createElement("ul");
  SOCIALS.forEach((social) => {
    const listItem = document.createElement("li");
    const link = document.createElement("a");
    externalLink(link, social.url, social.name);
    listItem.appendChild(link);
    socialsList.appendChild(listItem);
  });
  socialsContainer.appendChild(socialsList);
};

const renderCopyright = function () {
  const copyrightText = document.createElement("p");
  // copyrightText.innerHTML = `&copy; ${YEAR} ${NAME}. All rights reserved.`;
  copyrightText.innerHTML = `&copy; ${YEAR}. All rights reserved.`;
  const copyrightContainer = document.getElementById(CONTAINERS.copyright);
  copyrightContainer.append(copyrightText);
};

export const footer = function () {
  const footer = document.getElementById("footer-container");
  footer.classList.add("container");
  renderSocials();
  renderCopyright();
};
