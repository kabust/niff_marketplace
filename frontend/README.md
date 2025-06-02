# NIFF Marketplace Frontend

A modern e-commerce platform frontend built with Vue 3 and Vite, designed for emerging streetwear designers.

## Features

- Modern, responsive UI design
- Dynamic product catalog with carousel navigation
- User authentication and profile management
- Shopping cart functionality
- Secure checkout process
- Designer portal for product management

## Tech Stack

- Vue 3 (Composition API)
- Vite
- Vue Router
- Pinia for state management
- ESLint for code quality
- Docker support for containerization

## Prerequisites

- Node.js (v16 or higher)
- npm (v8 or higher)
- Docker (optional, for containerized development)

## Development Setup

1. Clone the repository
2. Install dependencies:
```sh
npm install
```

3. Start the development server:
```sh
npm run dev
```

The app will be available at `http://localhost:5173`

## Docker Setup

Build and run the frontend container:

```sh
docker build -t niff-frontend .
docker run -p 80:80 niff-frontend
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run ESLint
- `npm run preview` - Preview production build locally

## Environment Variables

Create a `.env` file in the root directory:

```env
VITE_API_URL=http://localhost:8000/api
```

## Project Structure

```
src/
├── assets/      # Static assets (images, styles)
├── components/  # Reusable Vue components
├── router/      # Vue Router configuration
├── services/    # API services
├── stores/      # Pinia stores
└── views/       # Page components
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request
