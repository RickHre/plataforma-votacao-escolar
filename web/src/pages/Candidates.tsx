import { For } from "solid-js";

import PageHeader from "../components/layout/PageHeader";

import Button from "../components/ui/Button";

import Card from "../components/ui/Card";

const candidates = [
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

export default function Candidates() {
    return (
        <div>
            <PageHeader
                title="Candidatos"
                description="Gerencie os candidatos da eleição"
                action={
                    <Button>Novo candidato</Button>
                }
            />
            <div class="admin-candidates">
                <For each={candidates}>
                    {(candidate) => (
                        <Card>
                            <div class="admin-candidate">
                                <div class="candidate-avatar">
                                    👤
                                </div>
                                <div>
                                    <h2>
                                        {candidate.name}
                                    </h2>
                                    <span>
                                        {candidate.description}
                                    </span>
                                </div>
                            </div>
                            <div class="candidate-actions">
                                <Button variant="secondary">Editar</Button>
                                <Button variant="danger">Remover</Button>
                            </div>
                        </Card>
                    )}
                </For>
            </div>
        </div>
    );
}
