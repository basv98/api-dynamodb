import aws_cdk as core
import aws_cdk.assertions as assertions

from tasks.tasks_stack import TasksStack

# example tests. To run these tests, uncomment this file along with the example
# resource in tasks/tasks_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TasksStack(app, "tasks")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
