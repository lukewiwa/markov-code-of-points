import { Stack, StackProps, Tags, Duration } from "aws-cdk-lib";
import { Construct } from "constructs";
import * as lambda from "aws-cdk-lib/aws-lambda";
import { PythonFunction } from "@aws-cdk/aws-lambda-python-alpha";
import * as events from "aws-cdk-lib/aws-events";
import * as targets from "aws-cdk-lib/aws-events-targets";
import * as path from "path";

const PROJECT_TAG = "cop-markov-twitter";

export class MarkovCodeOfPointsCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const CoPFn = new PythonFunction(this, "CoPMarkovTwitterFunction", {
      runtime: lambda.Runtime.PYTHON_3_8,
      entry: path.join(__dirname, "..", "..", "src"),
      environment: {
        TWITTER_CONSUMER_KEY: process.env.TWITTER_CONSUMER_KEY ?? "",
        TWITTER_CONSUMER_SECRET: process.env.TWITTER_CONSUMER_SECRET ?? "",
        TWITTER_TOKEN: process.env.TWITTER_TOKEN ?? "",
        TWITTER_TOKEN_SECRET: process.env.TWITTER_TOKEN_SECRET ?? "",
      },
      timeout: Duration.seconds(10),
    });

    const CoPFnRule = new events.Rule(this, "CoPMarkovTwitterSchedule", {
      schedule: events.Schedule.cron({
        minute: "20",
      }),
      targets: [new targets.LambdaFunction(CoPFn)],
    });

    Tags.of(CoPFn).add("project", PROJECT_TAG);
    Tags.of(CoPFnRule).add("project", PROJECT_TAG);
  }
}
