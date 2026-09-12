/* @refresh reload */
import { render } from "solid-js/web";

import App from "./App";

import "./styles/variables.css";
import "./styles/global.css";
import "./styles/components.css";
import "./styles/pages.css";

const root = document.getElementById("root");

if (!root) {
    throw new Error("Elemento #root não encontrado.");
}

render(() => <App />, root);
