import React, { useEffect } from "react";
import { AppProps } from "next/app";

import 'animate.css';
import "../styles/index.css";

function MyApp({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />;
}

export default MyApp;
