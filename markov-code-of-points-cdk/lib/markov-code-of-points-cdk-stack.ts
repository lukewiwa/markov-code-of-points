import * as cdk from "@aws-cdk/core";
import * as lambda from "@aws-cdk/aws-lambda";
import { PythonFunction } from "@aws-cdk/aws-lambda-python";
import * as events from "@aws-cdk/aws-events";
import * as targets from "@aws-cdk/aws-events-targets";
import * as path from "path";

const PROJECT_TAG = "cop-markov-twitter";

export class MarkovCodeOfPointsCdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
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
      timeout: cdk.Duration.seconds(10),
      architecture: lambda.Architecture.ARM_64
    });

    const CoPFnRule = new events.Rule(this, "CoPMarkovTwitterSchedule", {
      schedule: events.Schedule.cron({
        minute: "20",
      }),
      targets: [new targets.LambdaFunction(CoPFn)],
    });

    cdk.Tags.of(CoPFn).add("project", PROJECT_TAG);
    cdk.Tags.of(CoPFnRule).add("project", PROJECT_TAG);
  }
}
