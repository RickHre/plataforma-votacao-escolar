import { For } from "solid-js";

import type { DashboardResult } from "../../types/dashboard";

type ResultsListProps = {
    results: DashboardResult[];
};

export default function ResultsList(
    props: ResultsListProps
) {
    return (
        <div class="results-list">
            <For each={props.results}>
                {(result) => (
                    <div class="result-row">
                        <span>
                            {result.name}
                        </span>
                        <div class="result-bar">
                            <div
                                class="result-bar-value"
                                style={{
                                    width: `${result.percentage}%`
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
    );
}
