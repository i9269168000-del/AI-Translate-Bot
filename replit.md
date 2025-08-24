# Flask Web Server

## Overview

This is a demonstration Flask web application that showcases fundamental web development concepts. The project implements a multi-page website with home, about, and contact pages, featuring form handling, error pages, and responsive design. It serves as a foundation for building more complex web applications with Flask.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Web Framework
- **Flask**: Lightweight Python web framework chosen for its simplicity and flexibility
- **Jinja2 Templates**: Template engine for rendering dynamic HTML content with template inheritance
- **Blueprint-less Structure**: Simple single-file architecture suitable for small applications

### Frontend Architecture
- **Bootstrap 5**: CSS framework for responsive design and consistent styling
- **Dark Theme**: Uses Replit's custom Bootstrap dark theme for modern appearance
- **Font Awesome**: Icon library for visual enhancements
- **Progressive Enhancement**: JavaScript adds interactive features without breaking core functionality

### Routing Structure
- **Static Routes**: Home (`/`) and About (`/about`) pages for content display
- **Form Handling**: Contact page (`/contact`) with GET/POST method support
- **Error Handling**: Custom 404 and 500 error pages for better user experience

### Session Management
- **Flask Sessions**: Simple session handling with secret key configuration
- **Flash Messages**: Temporary message system for user feedback on form submissions

### Static File Organization
- **CSS**: Custom styling in `/static/css/style.css` for theme customization
- **JavaScript**: Client-side enhancements in `/static/js/script.js` for form validation and UX improvements

### Form Processing
- **Server-side Validation**: Basic form validation with flash message feedback
- **No Database**: Form submissions are acknowledged but not persisted (suitable for demo purposes)
- **CSRF Protection**: Implicit protection through Flask's session management

### Error Handling Strategy
- **Graceful Degradation**: Custom error pages maintain site navigation and branding
- **Debug Mode**: Development-friendly error logging and debugging enabled
- **User-friendly Messages**: Clear error explanations with actionable next steps

## External Dependencies

### CDN Resources
- **Bootstrap CSS**: `cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css` for responsive framework
- **Font Awesome**: `cdnjs.cloudflare.com` for icon fonts
- **No Database Dependencies**: Application runs without external database connections

### Python Packages
- **Flask**: Core web framework
- **Standard Library**: Uses built-in Python modules for logging and environment variables

### Environment Configuration
- **SESSION_SECRET**: Environment variable for session security (falls back to development default)
- **Debug Mode**: Enabled for development with auto-reload capabilities
- **Host Configuration**: Configured for Replit hosting on `0.0.0.0:5000`

### Development Tools
- **Logging**: Configured for debugging and development monitoring
- **Hot Reload**: Flask development server with auto-restart on file changes