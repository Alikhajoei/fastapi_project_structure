# FastAPI "Best-of-the-Best" Structure (Async + PostgreSQL)

This document explains a production-ready project structure for
**FastAPI** using:

-   Async endpoints
-   PostgreSQL
-   SQLAlchemy 2.0 Async
-   asyncpg
-   Layered Architecture (MVC + Clean Architecture principles)

The goals:

-   Keep routes/controllers thin\
-   Keep business logic isolated and testable\
-   Keep database code contained\
-   Make the project scalable and maintainable

------------------------------------------------------------------------

# 1. Full Folder Structure

    app/
      main.py

      api/
        deps.py
        v1/
          router.py
          endpoints/
            users.py

      schemas/
        user.py

      domain/
        services/
          user_service.py

      infrastructure/
        db/
          base.py
          session.py
          models/
            user_model.py
        repositories/
          user_repo.py

      core/
        config.py

------------------------------------------------------------------------

# 2. Architecture Overview

This structure separates the application into clear layers:

## API Layer (Controllers)

Location: `app/api/`

Responsibilities: - Define HTTP routes - Validate requests - Call
services - Return responses

Should NOT: - Write SQL queries - Contain business rules - Handle
database sessions directly

------------------------------------------------------------------------

## Schema Layer (Views / DTOs)

Location: `app/schemas/`

Responsibilities: - Define request models (UserCreate) - Define response
models (UserOut) - Control what data is exposed externally

Why important: - Prevent leaking database models - Maintain clean API
contracts - Auto-generate Swagger documentation

------------------------------------------------------------------------

## Domain Layer (Business Logic)

Location: `app/domain/`

Responsibilities: - Enforce business rules - Coordinate operations -
Decide application behavior

Examples: - Prevent duplicate emails - Hash passwords - Validate
business constraints

Important: This layer should ideally be framework-independent.

------------------------------------------------------------------------

## Infrastructure Layer (Database & External Systems)

Location: `app/infrastructure/`

Responsibilities: - SQLAlchemy models - Async database sessions -
Repository implementations - External services integration

Rule: Database-specific code must stay here.

------------------------------------------------------------------------

## Core Layer

Location: `app/core/`

Responsibilities: - Application configuration - Logging setup - Shared
utilities

------------------------------------------------------------------------

# 3. Request Flow (How Everything Works Together)

Example: POST /api/v1/users

1.  Client sends JSON request
2.  FastAPI validates using Pydantic schema
3.  Controller receives validated data
4.  Controller gets UserService via dependency injection
5.  Service checks business rules
6.  Service calls repository
7.  Repository performs async database query
8.  Service returns result
9.  Controller returns response model

Clean and predictable flow.

------------------------------------------------------------------------

# 4. Why This Structure Is Production-Ready

## Clear Separation of Concerns

Each layer has a single responsibility.

## Scalability

You can add new modules like: - orders - payments - auth

Without restructuring the whole project.

## Testability

-   Services can be unit tested without FastAPI
-   Repositories can be tested against a test database

## Maintainability

-   No "god files"
-   Clean boundaries
-   Easier onboarding for new developers

------------------------------------------------------------------------

# 5. Async + PostgreSQL Best Practices

-   Use asyncpg driver
-   Use SQLAlchemy 2.0 async engine
-   Use select() queries
-   Avoid blocking calls inside async endpoints
-   Use Alembic for migrations (not create_all in production)
-   Configure connection pooling for high load

------------------------------------------------------------------------

# 6. Suggested Production Improvements

To make it enterprise-ready:

-   Add Alembic migrations
-   Add JWT authentication module
-   Add structured logging
-   Add centralized error handling
-   Add pytest + async API tests
-   Add Docker support
-   Add CI/CD pipeline

------------------------------------------------------------------------

# 7. Summary

This architecture provides:

-   Clean layering
-   High scalability
-   Better testing
-   Clear boundaries
-   Async performance with PostgreSQL

It is a strong default for real-world SaaS and startup projects.

------------------------------------------------------------------------
