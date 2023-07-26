import React, {useState} from "react";
import Layout from "../components/Layout";

import FileSubmit from "../components/Tool/FileSubmit";
import RepoImport from "../components/Tool/RepoImport";

const tool: React.FC = () => { 
  return (
    <Layout title="Tool | Tool">
      <div className="flex justify-center h-auto min-h-screen p-10 mb-12 bg-white">
        <div className="w-full max-w-7xl">
          <RepoImport />
          <div className="flex justify-center my-2 md:my-4">
            <p className="text-xl font-thin md:text-2xl">Or</p>
          </div>
          <FileSubmit />
        </div>
      </div>
    </Layout>
  );
}
export default tool;

