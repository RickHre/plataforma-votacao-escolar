import type { User } from "../types/auth";
import { api } from "./api";

export interface LoginRequest {
    username: string;
    password: string;
}

export function login(
    data: LoginRequest
) {
    return api<User>(
        "/auth/login",
        {
            method: "POST",
            body: JSON.stringify(data)
        }
    );
}
