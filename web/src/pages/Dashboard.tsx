import PageHeader from "../components/layout/PageHeader";

import StatCard from "../components/dashboard/StatCard";

import ResultsList from "../components/dashboard/ResultsList";

import ParticipationCard from "../components/dashboard/ParticipationCard";

import Card from "../components/ui/Card";

import Button from "../components/ui/Button";

const results = [
    {
        candidateId: 1,
        name: "Candidato A",
        votes: 45,
        percentage: 45
    },
    {
        candidateId: 2,
        name: "Candidato B",
        votes: 35,
        percentage: 35
    },
    {
        candidateId: 3,
        name: "Candidato C",
        votes: 20,
        percentage: 20
    }
];

export default function Dashboard() {
    return (
        <div>
            <PageHeader
                title="Dashboard"
                description="Visão geral da eleição"
                action={ <Button>Atualizar</Button> }
            />
            <section class="stats-grid">
                <StatCard
                    title="Alunos"
                    value="120"
                    description="Cadastrados"
                />
                <StatCard
                    title="Votos"
                    value="100"
                    description="Registrados"
                />
                <StatCard
                    title="Candidatos"
                    value="3"
                    description="Cadastrados"
                />
                <StatCard
                    title="Participação"
                    value="85%"
                    description="Dos alunos"
                />
            </section>
            <section class="dashboard-grid">
                <Card>
                    <div class="card-header">
                        <h2>
                            Apuração
                        </h2>
                    </div>
                    <ResultsList results={results}/>
                </Card>

                <ParticipationCard percentage={85}/>
            </section>
            <section class="dashboard-grid">
                <Card>
                    <div class="card-header">
                        <h2>
                            Resultados recentes
                        </h2>
                    </div>
                    <ResultsList results={results}/>
                </Card>
                <Card>
                    <div class="card-header">
                        <h2>
                            Ações rápidas
                        </h2>
                    </div>
                    <div class="quick-actions">
                        <Button>
                            Gerenciar alunos
                        </Button>
                        <Button variant="secondary">
                            Cadastrar candidato
                        </Button>
                        <Button variant="secondary">
                            Apurar votos
                        </Button>
                    </div>
                </Card>
            </section>
        </div>
    );
}
