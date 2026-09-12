import type { Student }
    from "../types/student";

import { api }
    from "./api";

export function getStudents() {
    return api<Student[]>(
        "/students"
    );
}
