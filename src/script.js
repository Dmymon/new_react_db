const neo4j = require('neo4j-driver');

const url = "neo4j+s://c0aaff18.databases.neo4j.io:7687";
const user = "neo4j";
const password = "QxsGn3K9xV0evBljmCodr8cysD4I763NN1A1_rUMwX4"

const driver = neo4j.driver(url, neo4j.auth.basic(user, password));

export function createNode(category, properties) {
  const session = driver.session();
  const result = session.run(`MERGE (n:${category} ${JSON.stringify(properties)}) RETURN n`);
  session.close();
  return result;
}

export function createRelationship(from, to) {
  const session = driver.session();
  const result = session.run(`MATCH (a), (b) WHERE ID(a) = ${from} AND ID(b) = ${to} MERGE (a)-[r:works_with]->(b) RETURN r`);
  session.close();
  return result;
}

export function getNodes(category) {
  const session = driver.session();
  const result = session.run(`MATCH (n:${category}) RETURN n`);
  session.close();
  return result;
}

export function getRelationships(from, to) {
  const session = driver.session();
  const result = session.run(`MATCH (a)-[r:works_with]->(b) WHERE ID(a) = ${from} AND ID(b) = ${to} RETURN r`);
  session.close();
  return result;
}

export function getSupport() {
  const session = driver.session();
  const result = session.run(`MATCH (n:Support) RETURN n`);
  session.close();
  return result;
}

export async function getTierLabels() {
    let result = "";
    const session = driver.session();
    try {
        result = (await session.run(`MATCH (n:tier_labels) RETURN n.name;`)).records;

    } catch (err){
        console.log("ERROR: "+ err);
    } finally {
        session.close();
    }
    return result;
  }