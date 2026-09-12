import { api }
    from "./api";

export interface CreateVoteRequest {
    candidateId: number;
}

export function createVote(
    data: CreateVoteRequest
) {
    return api(
        "/votes",
        {
            method: "POST",
            body: JSON.stringify(data)
        }
    );
}
