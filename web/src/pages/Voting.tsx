import { createSignal, For } from "solid-js";

import CandidateCard
    from "../components/candidates/CandidateCard";

import Button
    from "../components/ui/Button";

import type { Candidate }
    from "../types/candidate";

const candidates: Candidate[] = [
    {
        id: 1,
        name: "Candidato A",
        description: "Chapa A"
    },
    {
        id: 2,
        name: "Candidato B",
        description: "Chapa B"
    },
    {
        id: 3,
        name: "Candidato C",
        description: "Chapa C"
    }
];

export default function Voting() {
    const [selected, setSelected] = createSignal<number | null>(null);

    function confirmVote() {
        if (selected() === null) {
            alert("Selecione um candidato.");
            return;
        }
        alert(`Voto: ${selected()}`);
    }

    return (
        <main class="voting-page">
            <div class="voting-container">
                <header class="voting-header">
                    <span>
                        Votação Escolar
                    </span>
                    <h1>
                        Escolha seu candidato
                    </h1>
                </header>
                <div class="candidate-grid">
                    <For each={candidates}>
                        {(candidate) => (
                            <CandidateCard
                                candidate={candidate}
                                selected={
                                    selected() === candidate.id
                                }
                                onSelect={() =>
                                    setSelected(candidate.id)
                                }
                            />
                        )}
                    </For>
                </div>
                <div class="voting-actions">
                    <Button onClick={confirmVote}>
                        Confirmar voto
                    </Button>
                </div>
            </div>
        </main>
    );
}
