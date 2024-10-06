𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐎𝐯𝐞𝐫𝐯𝐢𝐞𝐰

This project is built using modern and efficient technologies for both the backend and frontend. It is designed to be scalable, maintainable, and easy to set up. Below is an overview of the stack and instructions to get started.

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
