-- Supabase schema for Oracle
create table users (
    id uuid primary key,
    email text unique not null,
    role text default 'creator',
    wallet text,
    plan text
);

create table videos (
    id uuid primary key default gen_random_uuid(),
    owner_id uuid references users(id),
    caption text,
    file_url text,
    status text default 'pending'
);

create table automations (
    id uuid primary key default gen_random_uuid(),
    type text,
    params jsonb,
    status text default 'idle'
);

create table payments (
    id uuid primary key,
    user_id uuid references users(id),
    amount numeric,
    currency text,
    status text
);
