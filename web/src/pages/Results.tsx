import { For } from "solid-js";

import Card from "../components/ui/Card";

const results = [
    {
        name: "Candidato A",
        percentage: 45
    },
    {
        name: "Candidato B",
        percentage: 35
    },
    {
        name: "Candidato C",
        percentage: 20
    }
];

export default function Results() {
    return (
        <main class="results-page">
            <Card>
                <div class="results-header">
                    <h1>
                        Resultado da Eleição
                    </h1>
                    <span>
                        Apuração atual
                    </span>
                </div>
                <div class="results-list">
                    <For each={results}>
                        {(result) => (
                            <div class="result-row">
                                <span>
                                    {result.name}
                                </span>
                                <div class="result-bar">
                                    <div
                                        class="result-bar-value"
                                        style={{
                                            width:
                                                `${result.percentage}%`
                                        }}
                                    />
                                </div>
                                <strong>
                                    {result.percentage}%
                                </strong>
                            </div>
                        )}
                    </For>
                </div>
                <div class="results-total">
                    Total de votos: 100
                </div>
            </Card>
        </main>
    );
}
