import React, { useState } from "react";

const Auth = ({ onLogin, onRegister }) => {
  const [isRegister, setIsRegister] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isRegister) {
      onRegister({ name, email, password });
    } else {
      onLogin({ email, password });
    }
  };

  return (
    <div className=" flex h-[60vh]">
      <img
        src="./illustration.png"
        alt=""
        className=" h-[100%] aspect-square object-cover"
      />
      <div className="max-w-md mx-auto p-4 border border-white border-[10px] text-white h-[100%]">
        <h2 className="text-2xl font-bold mb-4">
          {isRegister ? "Register" : "Login"}
        </h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          {isRegister && (
            <input
              type="text"
              placeholder="Name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full p-2 border-b border-gray-300  bg-transparent"
            />
          )}
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full p-2 border-b border-gray-300  bg-transparent"
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full p-2 border-b border-gray-300  bg-transparent"
          />
          <button
            type="submit"
            className="w-full bg-blue-500 text-white p-2 rounded"
          >
            {isRegister ? "Register" : "Login"}
          </button>
          <button
            type="button"
            className="text-sm text-blue-500"
            onClick={() => setIsRegister(!isRegister)}
          >
            {isRegister
              ? "Already have an account? Login"
              : "No account? Register"}
          </button>
        </form>
      </div>
    </div>
  );
};

export default Auth;
