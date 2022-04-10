import React, { ReactElement } from "react";
import { render } from "react-dom";

function App(): ReactElement {
  return <h1>Hello World!</h1>;
}

render(<App />, document.getElementById("root"));
