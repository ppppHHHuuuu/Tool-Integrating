import React, { useState, useEffect } from "react";
import Link from "next/link";

const Header: React.FC = () => {
  const [scroll, setScroll] = useState<Boolean>(false);
  const [isNavOpen, setNavOpen] = useState<Boolean>(true);

  // Function to toggle the navigation menu
  const toggleNav = () => {
    console.log("nav toggled");
    setNavOpen(!isNavOpen);
  };

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 0) {
        setScroll(true);
      } else {
        setScroll(false);
      }
    };

    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <header
      className={`animate__animated animate__fadeInDown flex flex-wrap lg:flex-nowrap items-center justify-between pl-15 sticky top-0 z-20 px-4 py-4 text-white shadow-xl duration-500 md:px-10 xl:px-40 ${
        scroll ? "bg-white" : "bg-slate-950"
      }`}
    >
        <div className="flex items-center duration-500">
          <Link
            href="../"
            className={`text-bold text-2xl ${
              scroll ? "text-slate-950" : "text-white"
            }`}
          >
            TOOL
          </Link>
        </div>
        <button
          onClick={toggleNav}
          className={`inline-flex items-center justify-center w-10 h-10 p-2 duration-500 lg:hidden 
            ${scroll ? "text-slate-950" : "text-white"
          }`}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth={1.5}
            stroke="currentColor"
            className="w-6 h-6"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
            />
          </svg>
        </button>
        <div className="w-full duration-500 xk:ml-60 lg:ml-40 md:justify-center md:content-center lg:grid">
          <ul className={`
          duration-500  animate__animated
          animate__animated flex flex-col p-4 mt-4 font-medium lg:mt-0 lg:flex-row lg:space-x-8 lg:border-0 lg:p-0 lg:dark:bg-gray-900 
            ${isNavOpen ? "flex animate__fadeInDown" : "hidden animate__fadeOutUp" }`
          }>
            <li className={`lg:hidden ${scroll ? "text-slate-950" : "text-white"}
                `}>
              <hr className="my-4"/>
            </li>
            <li>
              <Link
                href="../coverage"
                className={`block font-normal pl-3 pr-4 duration-500 rounded 
                ${scroll ? "text-slate-950" : "text-white"}
                ${isNavOpen ? "hover:pl-4" : "" }
                `}>
                Coverage
              </Link>
            </li>
            <li>
              <Link
                href="../pricing"
                className={`block font-normal pl-3 pr-4 duration-500 rounded 
                ${scroll ? "text-slate-950" : "text-white"}
                ${isNavOpen ? "hover:pl-4" : "" }
                `}>
                Pricing
              </Link>
            </li>
            <li>
              <Link
                href="../about"
                className={`block font-normal pl-3 pr-4 duration-500 rounded 
                ${scroll ? "text-slate-950" : "text-white"}
                ${isNavOpen ? "hover:pl-4" : "" }
                `}>
                About
              </Link>
            </li>
            <li>
              <Link
                href="../tool"
                className={`block font-normal pl-3 pr-4 duration-500 rounded
                ${scroll ? "text-slate-950" : "text-white"}
                ${isNavOpen ? "hover:pl-4" : "" }
                `}>
                Tool
              </Link>
            </li>

            <li className={`my-2 lg:hidden ${scroll ? "text-slate-950" : "text-white"}
                `}>
              <hr className="my-4"/>
            </li>
            <li className="lg:hidden">
              <Link
                href="../login"
                className={`block font-normal pl-3 pr-4 duration-500 rounded
                ${scroll ? "text-slate-950" : "text-white"}
                ${isNavOpen ? "hover:pl-4" : "" }
                `}>
                Login
              </Link>
            </li>
            <li className="lg:hidden">
              <Link
                href="../signup"
                className={`block font-normal pl-3 pr-4 duration-500 rounded
                ${scroll ? "text-slate-950" : "text-white"}
                ${isNavOpen ? "hover:pl-4" : "" }
                `}>
                Sign up
              </Link>
            </li>
            
          </ul>
        </div>
        <div className="flex-col-reverse items-end hidden duration-500 w-96 lg:flex">
          <div>
            <button
              className={`mr-2 border px-6 py-1 duration-500 hover:text-slate-950 ${
                scroll
                  ? "border-slate-950 text-slate-950 hover:bg-slate-950 hover:text-white"
                  : "border-white hover:bg-white hover:text-slate-950"
              }`}
            >
              <Link href="../login">Login</Link>
            </button>
            <button
              className={`border px-6 py-1 duration-500 ${
                scroll
                  ? "border-slate-950 bg-slate-950 text-white hover:bg-white hover:text-slate-950"
                  : "bg-white text-slate-950 hover:bg-slate-950 hover:text-white"
              }`}
            >
              <Link href="../signup">Sign up</Link>
            </button>
          </div>
        </div>
    </header>
  );
};

export default Header;
