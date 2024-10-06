𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐎𝐯𝐞𝐫𝐯𝐢𝐞𝐰

This project is built using modern and efficient technologies for both the backend and frontend. It is designed to be scalable, maintainable, and easy to set up. Below is an overview of the stack and instructions to get started.

𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧

Is a real-time cryptocurrency tracking platform built with a modern tech stack. It integrates with a third-party API to monitor and display the top 100 most popular cryptocurrencies, providing users with concise and up-to-date information on each coin.

𝐊𝐞𝐲 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬:

.𝐑𝐞𝐚𝐥-𝐓𝐢𝐦𝐞 𝐃𝐚𝐭𝐚:

Using an integrated API, the project fetches the latest data on the top 100 cryptocurrencies, including price, market cap, and volume, ensuring users always have the most accurate information.

.𝐂𝐚𝐜𝐡𝐢𝐧𝐠 𝐒𝐮𝐩𝐩𝐨𝐫𝐭:

To enhance performance and reduce unnecessary API calls, the project implements caching mechanisms that store data temporarily, improving load times and efficiency.

.𝐔𝐬𝐞𝐫-𝐅𝐫𝐢𝐞𝐧𝐝𝐥𝐲 𝐈𝐧𝐭𝐞𝐫𝐟𝐚𝐜𝐞: 

The frontend, built with React, provides a clean and intuitive interface, making it easy for users to browse and track cryptocurrency trends.

This project is ideal for users looking to stay updated on the rapidly changing crypto market, with the added benefit of smooth performance thanks to caching.

𝐓𝐞𝐜𝐡 𝐒𝐭𝐚𝐜𝐤

𝐁𝐚𝐜𝐤𝐞𝐧𝐝:

FastAPI – a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

Pydantic – for data validation using Python's type annotations.

pydantic-settings – a powerful library for managing configuration and environment variables.

aiohttp – an asynchronous HTTP client/server framework.

alru_cache – async LRU cache for caching heavy computations or requests.

𝐅𝐫𝐨𝐧𝐭𝐞𝐧𝐝:

React – a JavaScript library for building user interfaces.

axios – for making HTTP requests to the backend.

Ant Design – a UI library that provides a set of high-quality React components out of the box.

Tailwind CSS – a utility-first CSS framework for building custom designs quickly.

𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐒𝐞𝐭𝐮𝐩

𝐁𝐚𝐜𝐤𝐞𝐧𝐝 𝐒𝐞𝐭𝐮𝐩:

Navigate to the backend folder:

cd backend

Run the backend development server using the following command:

uvicorn src.main:app --reload

This command starts the FastAPI server in development mode with live reloading.

𝐅𝐫𝐨𝐧𝐭𝐞𝐧𝐝 𝐒𝐞𝐭𝐮𝐩:

Create a new Vite project by running:

npm create vite@latest

Install all required dependencies:

npm install

Start the development server:

npm run dev

This command launches the frontend development server.

𝐀𝐝𝐝𝐢𝐭𝐢𝐨𝐧𝐚𝐥 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧

The backend is designed to work asynchronously to handle high concurrency with minimal resource usage.

React is used on the frontend for fast and efficient UI rendering, along with Tailwind for flexible and responsive design.

Feel free to contribute, open issues, or suggest improvements. Let's build something awesome together!
