// tailwind.config.js
module.exports = {
    content: [
      '/Users/palastha/Desktop/CSUI/PBP/consign-pbp/templates/**/*.html', // Define the paths to all of your HTML/JS files
    ],
    theme: {
      extend: {},
    },
    plugins: [
      require('@tailwindcss/aspect-ratio'), // Add the plugin here
    ],
  }
