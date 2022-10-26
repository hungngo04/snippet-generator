import * as lambda from 'aws-cdk-lib/aws-lambda';
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib'

export class InfrastructureStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const apiLambda = new lambda.Function(this, "ApiFunction", {
      runtime: lambda.Runtime.PYTHON_3_9,
      code: lambda.Code.fromAsset("../app/"),
      handler: 
    })
  }
}
