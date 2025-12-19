from agent import LeadScraperAgent

if __name__ == "__main__":
    agent = LeadScraperAgent()
    result = agent.run("data/apollo_sample.csv")
    print(result)
