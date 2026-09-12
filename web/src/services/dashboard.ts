import type {
    DashboardStats,
    DashboardResult
} from "../types/dashboard";

import { api }
    from "./api";

export function getDashboardStats() {
    return api<DashboardStats>(
        "/dashboard/stats"
    );
}

export function getDashboardResults() {
    return api<DashboardResult[]>(
        "/dashboard/results"
    );
}
