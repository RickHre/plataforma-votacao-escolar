import type { Candidate }
    from "../types/candidate";

import { api }
    from "./api";

export function getCandidates() {
    return api<Candidate[]>(
        "/candidates"
    );
}
