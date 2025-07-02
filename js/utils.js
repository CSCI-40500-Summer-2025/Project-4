/*
 * File: utils.js
 * Author: Ragib Asif
 * Email: ragib.asif30@myhunter.cuny.edu
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 */

export function externalLink(item, url, text) {
  item.href = url;
  item.target = "_blank";
  item.rel = "noopener noreferrer";
  item.innerText = text;
  item.classList.add("external-link");
}
