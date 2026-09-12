export interface DashboardResult {
    candidateId: number;
    name: string;
    votes: number;
    percentage: number;
}

export interface DashboardStats {
    students: number;
    votes: number;
    candidates: number;
    participation: number;
}
