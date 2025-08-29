/** @type {import('tailwindcss').Config} */
export default {
    content: ["./index.html", "./src/**/*.{js,jsx}"],
    darkMode: "class",
    theme: {
      extend: {
        colors: {
          darkbg: "#0d1117",
          darkcard: "#161b22",
          primary: "#58a6ff"
        }
      }
    },
    plugins: [],
  };
  