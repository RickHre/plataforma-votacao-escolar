import {
    createSignal
} from "solid-js";

import type { User }
    from "../types/auth";

const [
    user,
    setUser
] = createSignal<User | null>(null);

export {
    user,
    setUser
};

export function isAuthenticated() {
    return user() !== null;
}

export function logout() {
    setUser(null);
}
