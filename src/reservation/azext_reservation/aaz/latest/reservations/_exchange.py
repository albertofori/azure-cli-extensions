# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "reservations exchange",
)
class Exchange(AAZCommand):
    """Returns one or more `Reservations` in exchange for one or more `Reservation` purchases.


    :example: Exchange reservations
        az reservations exchange --session-id 40000000-aaaa-bbbb-cccc-200000000012
    """

    _aaz_info = {
        "version": "2022-03-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.capacity/exchange", "2022-03-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.session_id = AAZStrArg(
            options=["--session-id"],
            arg_group="Properties",
            help="SessionId that was returned by CalculateExchange API.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ExchangePost(ctx=self.ctx)()
        self.post_operations()

    # @register_callback
    def pre_operations(self):
        pass

    # @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ExchangePost(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Capacity/exchange",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("sessionId", AAZStrType, ".session_id")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.error = AAZObjectType()
            _schema_on_200.id = AAZStrType()
            _schema_on_200.name = AAZStrType()
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.status = AAZStrType()

            error = cls._schema_on_200.error
            error.code = AAZStrType()
            error.message = AAZStrType()

            properties = cls._schema_on_200.properties
            properties.net_payable = AAZObjectType(
                serialized_name="netPayable",
            )
            _build_schema_price_read(properties.net_payable)
            properties.policy_result = AAZObjectType(
                serialized_name="policyResult",
            )
            properties.purchases_total = AAZObjectType(
                serialized_name="purchasesTotal",
            )
            _build_schema_price_read(properties.purchases_total)
            properties.refunds_total = AAZObjectType(
                serialized_name="refundsTotal",
            )
            _build_schema_price_read(properties.refunds_total)
            properties.reservations_to_exchange = AAZListType(
                serialized_name="reservationsToExchange",
            )
            properties.reservations_to_purchase = AAZListType(
                serialized_name="reservationsToPurchase",
            )
            properties.session_id = AAZStrType(
                serialized_name="sessionId",
            )

            policy_result = cls._schema_on_200.properties.policy_result
            policy_result.policy_errors = AAZListType(
                serialized_name="policyErrors",
            )

            policy_errors = cls._schema_on_200.properties.policy_result.policy_errors
            policy_errors.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.policy_result.policy_errors.Element
            _element.code = AAZStrType()
            _element.message = AAZStrType()

            reservations_to_exchange = cls._schema_on_200.properties.reservations_to_exchange
            reservations_to_exchange.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.reservations_to_exchange.Element
            _element.billing_information = AAZObjectType(
                serialized_name="billingInformation",
            )
            _element.billing_refund_amount = AAZObjectType(
                serialized_name="billingRefundAmount",
            )
            _build_schema_price_read(_element.billing_refund_amount)
            _element.quantity = AAZIntType()
            _element.reservation_id = AAZStrType(
                serialized_name="reservationId",
            )
            _element.status = AAZStrType()

            billing_information = cls._schema_on_200.properties.reservations_to_exchange.Element.billing_information
            billing_information.billing_currency_prorated_amount = AAZObjectType(
                serialized_name="billingCurrencyProratedAmount",
            )
            _build_schema_price_read(billing_information.billing_currency_prorated_amount)
            billing_information.billing_currency_remaining_commitment_amount = AAZObjectType(
                serialized_name="billingCurrencyRemainingCommitmentAmount",
            )
            _build_schema_price_read(billing_information.billing_currency_remaining_commitment_amount)
            billing_information.billing_currency_total_paid_amount = AAZObjectType(
                serialized_name="billingCurrencyTotalPaidAmount",
            )
            _build_schema_price_read(billing_information.billing_currency_total_paid_amount)

            reservations_to_purchase = cls._schema_on_200.properties.reservations_to_purchase
            reservations_to_purchase.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.reservations_to_purchase.Element
            _element.billing_currency_total = AAZObjectType(
                serialized_name="billingCurrencyTotal",
            )
            _build_schema_price_read(_element.billing_currency_total)
            _element.properties = AAZObjectType()
            _element.reservation_id = AAZStrType(
                serialized_name="reservationId",
            )
            _element.reservation_order_id = AAZStrType(
                serialized_name="reservationOrderId",
            )
            _element.status = AAZStrType()

            properties = cls._schema_on_200.properties.reservations_to_purchase.Element.properties
            properties.location = AAZStrType()
            properties.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            properties.sku = AAZObjectType()

            properties = cls._schema_on_200.properties.reservations_to_purchase.Element.properties.properties
            properties.applied_scope_type = AAZStrType(
                serialized_name="appliedScopeType",
            )
            properties.applied_scopes = AAZListType(
                serialized_name="appliedScopes",
            )
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.billing_scope_id = AAZStrType(
                serialized_name="billingScopeId",
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.quantity = AAZIntType()
            properties.renew = AAZBoolType()
            properties.reserved_resource_properties = AAZObjectType(
                serialized_name="reservedResourceProperties",
            )
            properties.reserved_resource_type = AAZStrType(
                serialized_name="reservedResourceType",
            )
            properties.term = AAZStrType()

            applied_scopes = cls._schema_on_200.properties.reservations_to_purchase.Element.properties.properties.applied_scopes
            applied_scopes.Element = AAZStrType()

            reserved_resource_properties = cls._schema_on_200.properties.reservations_to_purchase.Element.properties.properties.reserved_resource_properties
            reserved_resource_properties.instance_flexibility = AAZStrType(
                serialized_name="instanceFlexibility",
            )

            sku = cls._schema_on_200.properties.reservations_to_purchase.Element.properties.sku
            sku.name = AAZStrType()

            return cls._schema_on_200


_schema_price_read = None


def _build_schema_price_read(_schema):
    global _schema_price_read
    if _schema_price_read is not None:
        _schema.amount = _schema_price_read.amount
        _schema.currency_code = _schema_price_read.currency_code
        return

    _schema_price_read = AAZObjectType()

    price_read = _schema_price_read
    price_read.amount = AAZFloatType()
    price_read.currency_code = AAZStrType(
        serialized_name="currencyCode",
    )

    _schema.amount = _schema_price_read.amount
    _schema.currency_code = _schema_price_read.currency_code


__all__ = ["Exchange"]
